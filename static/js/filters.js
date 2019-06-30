$(document).ready(function () {

    /**
     * Variables
     */
    let pages = [];
    let searchResults = [];
    let paginationActivePage = 1;

    /**
     * Fetches results to display when select or input filed is changed
     */

    $("select, input").change(function () {
        fetchResults();
    });

    /**
     * Function collects user input into search filters, and sends this to 
     * back end to be processed. When the filtered results are returned it 
     * starts the process to display the data in the browser.
     */
    function fetchResults() {

        let location = $("#townSelect").val();
        let category = $("#categorySelect").val();
        let days = $("#daysFilter").val();
        let inOut = $("#inOutFilter").val();

        let ageRangeCheckboxes = $('.age-range-js');
        let ageRangeIds = getCheckedIds(ageRangeCheckboxes);
        let otherDetailsCheckboxes = $('.in-out-js');
        let otherIds = getCheckedIds(otherDetailsCheckboxes);

        const data = {
            location: location,
            category: category,
            days: days,
            inOut: inOut,
            ageRangeIds: ageRangeIds,
            otherIds: otherIds,
        };

        showLoading();

        fetch('/activities', {
                method: 'POST',
                cors: '*same-origin',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            })
            .then(res => res.json())
            .then(data => {
                hideLoading();
                searchResults = [];
                getFullData(data);
            })
            .catch(err => {
                hideLoading();
                alertModal('error');
                console.log(err);
            });
    }

    /**
     * Takes search results data from fetch and pushes it into an array
     * that an be accessed outside of the fetch function.
     * @param {array} data 
     */

    function getFullData(data) {
        let numResults = data.length;
        for (let i = 0; i < numResults; i++) {
            searchResults.push(data[i]);
        }
        $('#num-of-results').text(numResults + ' results');
        displayResults(data);
    }

    /**
     * Function takes data sent from python, breaks results into groups of 12
     * for pagination. Prints out html pagination icons if needed, or removes them if not. 
     * prints out first page (or all results if 12 or less) to the screen.
     * @param {arr} data 
     */
    function displayResults(data) {
        pages = pages_fcn(data, 12);
        let numOfPages = pages.length;

        if (numOfPages > 1) {
            const paginationString = buildPagination(numOfPages);
            $('#pagination-js').html(paginationString);

            $('.page-item#pg-1').addClass('active');
            paginationActivePage = 1;
            /* adds onclick event for pagination once html for it has been inserted */
            $('.page-js').click(function() {
                let this_id = this.id;
                $('.page-js').parent().removeClass('active');
                $(this).parent().addClass('active');
                displayPages(this_id, numOfPages);
            })

            let page1 = Object.values(pages[0]);
            page1 = page1[0];
            buildSearchResultsString(page1);
            return;
        } else {
            $('#pagination-js').html('');

            let single_page = Object.values(pages[0]);
            single_page = single_page[0];
            buildSearchResultsString(single_page);
            return;
        }
    }

    function displayPages(page, numOfPages) {
        console.log(page);
        let pg_index = '';
        if (page != "prev" && page != "next") {
            pg_index = parseInt(page) - 1;
            paginationActivePage = pg_index + 1;
        } else if (page == "prev" && paginationActivePage != 1) {
            paginationActivePage--;
            pg_index = paginationActivePage - 1;
            $('.page-js').parent().removeClass('active');
            let pgSelector = '.page-item#pg-'+ paginationActivePage;
            $(pgSelector).addClass('active');
            
        } else if (page == "next" && paginationActivePage != numOfPages) {
            paginationActivePage++;
            pg_index = paginationActivePage - 1;
            $('.page-js').parent().removeClass('active');
            let pgSelector = '.page-item#pg-'+ paginationActivePage;
            $(pgSelector).addClass('active');
        } else {
            return;
        }

        let result = Object.values(pages[pg_index]);
        result = result[0];
        buildSearchResultsString(result);
    }

    /**
     * Builds html string for number of pages needed in pagination.
     * @param {int} num | number of pages needed
     */

    function buildPagination(num) {
        let paginationSubString = '';
        for (let i = 0; i < num; i++) {
            let paginate = `
            <li id="pg-${i + 1}" class="page-item"><a id="${i + 1}" class="page-link page-js" href="#">${i + 1}</a></li>
            `;
            paginationSubString += paginate;
        }

        const paginationString = `
        <nav aria-label="Pagination">
            <ul class="pagination justify-content-center">
                <li id="pg-prev" class="page-item">
                    <a id="prev" class="page-link page-js" aria-label="Previous" href="#">
                        <span aria-hidden="true">&laquo;</span>
                    </a>
                </li>
                ${paginationSubString}
                <li id="pg-next" class="page-item">
                    <a id="next" class="page-link page-js" aria-label="Next" href="#">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                </li>
            </ul>
        </nav>
        `;
        return paginationString;
    }

    /**
     * Function takes an array and a number, breaks up the array of search results and returns
     * an array of objects to be used for pages in pagination.
     * @param {array} arr 
     * @param {int} n 
     */
    function pages_fcn(arr, n) {
        let a = arr;
        let pages_arr = [];
        let i = 1;
        do {
            let chunk = a.splice(0, n);
            let pageNum = 'page' + i.toString();
            let obj = {
                [pageNum]: chunk
            };
            pages_arr.push(obj);
            i++;
        }
        while (a.length > 0);
        return pages_arr;
    }

    /**
     * Takes array of search results, and loops through them to add the data to a html block
     * for each card to display the search results
     * @param {array} searchResults 
     */

    function buildSearchResultsString(searchResults) {
        let searchResultsString = '';
        for (let i = 0; i < searchResults.length; i++) {
            let card = cardTemplate(searchResults[i]);
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
        let id_string = searchResult._id.$oid;
        let href = "/listing/" + searchResult.title + '?activity_id=' + id_string;

        const card = `
        <div class="col-12 col-sm-6 col-lg-4 col-xl-3">
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
                    <a class="readmore-link" href="${href}">Read More <i class="fas fa-arrow-circle-right"></i></a>
                </div>
            </div>
        </div>
        `;
        return card;
    }

    /**
     * Clears all checked filters and selected options on search page,
     * then reloads all results from the database.
     */

    $('.clear-filters').click(function () {
        let inputs = $('input');
        let options = $('option');
        options.each(function () {
            $(this).prop('selected', false);
        });
        inputs.each(function () {
            $(this).prop('checked', false);
        });
        fetchResults();
    });

    function getCheckedIds(input) {
        let ids = [];
        input.each(function () {
            if ($(this).prop("checked") == true) {
                ids.push(this.id);
            }
        });
        return ids;
    }


    /* Code credit: For animated side-nav taken from 
    https://www.w3schools.com/howto/howto_js_sidenav.asp 
    and edited to fit project needs as a pull out filters bar */

    $('.closeFiltersBtn').click(function () {
        closeFilters();
    });

    $('#openFiltersBtn').click(function () {
        openFilters();
    });

    function openFilters() {
        $('#filter-nav, main, footer, nav').addClass('filters-open');
    }

    function closeFilters() {
        $('#filter-nav, main, footer, nav').removeClass('filters-open');
    }

    fetchResults();

});