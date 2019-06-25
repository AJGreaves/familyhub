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

    $('.clear-filters').click(function() {
        inputs = $('input')
        inputs.each(function() {
            $(this).prop('checked', false);
        })
    })

});