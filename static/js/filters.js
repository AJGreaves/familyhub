$(document).ready(function () {

    /**
     * Get data from api to display in activities page
     */

    showLoading();
    fetch('/api/activities')
        .then(res => res.json())
        .then(data => {
            getFullData(data);
        })
        .then(hideLoading())
        .catch(err => {
            hideLoading();
            alertModal('error');
            console.log(err);
        });

    let fullDataArray = []

    function getFullData(data) {
        for (i = 0; i < data.length; i++) {
            fullDataArray.push(data[i]);
        }
        getDisplayArray(fullDataArray);
    }

    let start = 0;
    let working = false;
    let searchResults = [];
    /**
     * Gets first 12 results from the data
     */
    function getDisplayArray(data) {
        for (i = start; i < start + 6; i++) {
            searchResults.push(data[i]);
        }
        start += 6
        buildSearchResultsString(searchResults);
        return;
    }

    /**
     * Takes array of search results, and loops through them to add the data to a html block
     * for each card to display the search results
     * @param {array} searchResults 
     */

    function buildSearchResultsString(searchResults) {
        let searchResultsString = ''
        for (i = 0; i < searchResults.length; i++) {
            card = cardTemplate(searchResults[i]);
            searchResultsString += card;
        }
        /**
         * inserts cards into the page
         */
        $('#searchResults').html(searchResultsString);
    }

    /**
     * Builds each card with the data from the array, then returns the card
     * to be added to the final string of html to be inserted into the page.
     * @param {array object} searchResult 
     */

    function cardTemplate(searchResult) {
        const card = `
        <div class="col-12 col-sm-6 col-lg-4">
            <div class="card familyhub-card">
                <div class="card-img-wrapper">
                    <!-- Inline style used here for ease of placing background image with JS -->
                    <div class="card-picture" title="${searchResult.title}" style="background-image: url(${searchResult.imgUrl})">
                        <div class="location-text">${searchResult.address.town}</div>
                    </div>
                </div>
                <div class="card-body">
                    <div class="card-title-wrapper">
                        <h4 class="card-title">${searchResult.title}</h4>
                    </div>
                    <div class="card-text-wrapper">
                        <p class="card-text">${searchResult.shortDescription}...</p>
                    </div>
                    <a class="readmore-link" href="{{ url_for('activity_listing_page', title=${searchResult.title}, activity_id=${searchResult._id})}}">Read More <i class="fas fa-arrow-circle-right"></i></a>
                </div>
            </div>
        </div>
        `
        return card;
    }

    /**
     * Loads more cards from data as the user scrolls. 
     * Code for this function taken from the following youtube
     * https://www.youtube.com/watch?v=76IANst0jwc
     */
    $(window).scroll(function () {
        if ($(this).scrollTop() + 1 >= $('body').height() - $(window).height()) {
            if (working == false) {
                working = true;
                getDisplayArray(fullDataArray);
                setTimeout(function () {
                    working = false;
                }, 1000)
            }
        }
    })

    /**
     * Clears all checked filters on search page
     */

    $('.clear-filters').click(function () {
        inputs = $('input')
        inputs.each(function () {
            $(this).prop('checked', false);
        })
    })

    $("input").change(function () {
        let locationInput = $('.location-checkboxes-js input');
        let categoriesInput = $('.categories-checkboxes-js input');
        let agesInput = $('.ages-checkboxes-js input');
        let daysInput = $('.days-checkboxes-js input');
        let inoutInput = $('.inout-checkboxes-js input');
        let otherInput = $('.other-checkboxes-js input');

        let locationIds = getCheckedIds(locationInput);
        let categoryIds = getCheckedIds(categoriesInput);
        let ageIds = getCheckedIds(agesInput);
        let dayIds = getCheckedIds(daysInput);
        let inoutIds = getCheckedIds(inoutInput);
        let otherIds = getCheckedIds(otherInput);

        let locationResults = getLocationResults(locationIds);
        let categoryResults = getCategoryResults(categoryIds);
        let ageResults = getAgeResults(ageIds);
        console.log(ageResults);
    });

    /**
     * works for location checkboxes in filters
     */
    function getLocationResults(locationIds) {
        let result = fullDataArray.filter(function (activity) {
            return locationIds.includes(activity.address.town);
        })
        return result;
    }

    function getCategoryResults(categoryIds) {
        results = [];
        for (i = 0; i < categoryIds.length; i++) {
            switch (categoryIds[i]) {
                case 'sports':
                    results.push(fullDataArray.filter(activity => activity.categories.sports));
                    break;
                case 'swimming':
                    results.push(fullDataArray.filter(activity => activity.categories.swimming));
                    break;
                case 'creative':
                    results.push(fullDataArray.filter(activity => activity.categories.creative));
                    break;
                case 'scienceTech':
                    results.push(fullDataArray.filter(activity => activity.categories.scienceTech));
                    break;
                case 'cultureMusic':
                    results.push(fullDataArray.filter(activity => activity.categories.cultureMusic));
                    break;
                case 'dramaDance':
                    results.push(fullDataArray.filter(activity => activity.categories.dramaDance));
                    break;
                case 'yogaMindfulness':
                    results.push(fullDataArray.filter(activity => activity.categories.yogaMindfulness));
                    break;
                case 'museumsExhibitions':
                    results.push(fullDataArray.filter(activity => activity.categories.museumsExhibitions));
                    break;
                case 'parksPlaygrounds':
                    results.push(fullDataArray.filter(activity => activity.categories.parksPlaygrounds));
                    break;
                case 'playgroups':
                    results.push(fullDataArray.filter(activity => activity.categories.playgroups));
                    break;
                case 'nature':
                    results.push(fullDataArray.filter(activity => activity.categories.nature));
                    break;
                case 'animals':
                    results.push(fullDataArray.filter(activity => activity.categories.animals));
                    break;
                case 'clubs':
                    results.push(fullDataArray.filter(activity => activity.categories.clubs));
                    break;
                case 'parties':
                    results.push(fullDataArray.filter(activity => activity.categories.parties));
                    break;
                default:
                    break;
            }
        }
        return results;
    }

    function getAgeResults(ageIds) {
        results = [];
        for (i = 0; i < ageIds.length; i++) {
            switch (ageIds[i]) {
                case 'under4':
                    results.push(fullDataArray.filter(activity => activity.ageRange.under4));
                    break;
                case 'age4to6':
                    results.push(fullDataArray.filter(activity => activity.ageRange.age4to6));
                    break;
                case 'age6to8':
                    results.push(fullDataArray.filter(activity => activity.ageRange.age6to8));
                    break;
                case 'age8to10':
                    results.push(fullDataArray.filter(activity => activity.ageRange.age8to10));
                    break;
                case 'age10to12':
                    results.push(fullDataArray.filter(activity => activity.ageRange.age10to12));
                    break;
                case 'age12up':
                    results.push(fullDataArray.filter(activity => activity.ageRange.age12up));
                    break;
                default:
                    break;
            }
        }
        return results;
    }

    function getCheckedIds(input) {
        ids = [];
        input.each(function () {
            if ($(this).prop("checked") == true) {
                ids.push(this.id);
            }
        })
        return ids;
    }

});

