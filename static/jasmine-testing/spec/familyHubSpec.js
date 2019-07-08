// tests for functions in common.js

describe('alertModal function', function () {

    beforeEach(() => {
        setFixtures(`
            <div id="alertModal">
                <h2 id="alertHeading"></h2>
                <p id="alertMessage"></p>
                <p id="alertMessageLine2"></p>
            </div>
            `);
    });

    it('should add text "Sorry" to #alertHeading', function () {
        alertModal('no user match');
        expect($('#alertHeading').text()).toEqual('Sorry');
    });

    it('should add text "No account with this username or email address.\n Please try again." to #alertMessage', function () {
        alertModal('no user match');
        expect($('#alertMessage').text()).toEqual('No account with this username or email address.\n Please try again.');
    });

    it('should add text "Error" to #alertHeading', function () {
        alertModal('start end dates wrong', '02/01/2019', '01/01/2019');
        expect($('#alertHeading').text()).toEqual('Error');
    });

    it('should add text "You input a finish date 01/01/2019" to #alertMessage', function () {
        alertModal('start end dates wrong', '02/01/2019', '01/01/2019');
        expect($('#alertMessage').text()).toEqual('You input a finish date 01/01/2019');
    });

    it('should add text "that is before your start date 02/01/2019" to #alertMessageLine2', function () {
        alertModal('start end dates wrong', '02/01/2019', '01/01/2019');
        expect($('#alertMessageLine2').text()).toEqual('that is before your start date 02/01/2019');
    });

    it('should add text "Sorry" to #alertHeading', function () {
        alertModal('no share');
        expect($('#alertHeading').text()).toEqual('Sorry');
    });

    it("should add text You can't share this page in preview mode. to #alertMessage", function () {
        alertModal('no share');
        expect($('#alertMessage').text()).toEqual("You can't share this page in preview mode.");
    });

    it('should add text "Once you have published it, the share links will work" to #alertMessageLine2', function () {
        alertModal('no share');
        expect($('#alertMessageLine2').text()).toEqual('Once you have published it, the share links will work');
    });

    it('should toggle .active class onto #alertModal', function () {
        alertModal('');
        expect($('#alertModal')).toHaveClass('active');
    })
})

describe('openLoggedInModal function', function () {

    beforeEach(() => {
        setFixtures(`
        <div id="loggedInModal">
            <h2 id="welcomeMessage"></h2>
            <a id="accountUrl" href="#">My listings</a>
            <a id="newActivityUrl" href="#">Add new activity</a>
        </div>
        `);
    });

    it('should add welcome message that includes username', function () {
        openLoggedInModal('Arthur Dent');
        expect($('#welcomeMessage').text()).toEqual('Welcome Arthur Dent.')
    });

    it('should create account page href url that includes username', function () {
        openLoggedInModal('Zaphod Beeblebrox');
        expect($("#accountUrl").attr('href')).toEqual('/account/zaphod-beeblebrox');
    });

    it('should create editor page href url that includes username', function () {
        openLoggedInModal('Slartibartfast');
        expect($("#newActivityUrl").attr('href')).toEqual('/editor/slartibartfast/add-new');
    });

    it('should add .active class to #loggedInModal', function () {
        openLoggedInModal('');
        expect($('#loggedInModal')).toHaveClass('active');
    })
})

describe('slugify function', function () {

    it('should return string with all capitals changed to lowercase', function () {
        let result = slugify('CAPITALS');
        expect(result).toEqual('capitals');
    });

    it('should return string with mix of capitals and lowercase changed to all lowercase', function () {
        let result = slugify('MyStrinG');
        expect(result).toEqual('mystring');
    });

    it('should return string where any spaces have been replaced with -', function () {
        let result = slugify('string with spaces in');
        expect(result).toEqual('string-with-spaces-in');
    });

    it('should remove all non-word characters', function () {
        let result = slugify('Lots%of$special*Charatersęǵḧ');
        expect(result).toEqual('lotsofspecialcharatersegh');
    });

    it('should replace & with "and"', function () {
        let result = slugify('bacon & eggs');
        expect(result).toEqual('bacon-and-eggs');
    });

    it('should trim - from start of text', function () {
        let result = slugify('-my slug');
        expect(result).toEqual('my-slug');
    });

    it('should trim - from end of text', function () {
        let result = slugify('my other slug-');
        expect(result).toEqual('my-other-slug');
    });
})


describe('capFirst function', function () {

    it('Should return string with first letter capitalised', function () {
        result = capFirst('bob');
        expect(result).toEqual('Bob');
    })
})

describe('showLoading function', function () {

    beforeEach(() => {
        setFixtures(`
        <div id="spinner-wrapper" style="visibility: hidden;">
            <div id="spinner" Title="loading"></div>
        </div>
        `);
    });

    it('should set style to visibility: visible on #spinner-wrapper', function () {
        showLoading();
        expect($("#spinner-wrapper").attr('style')).toEqual('visibility: visible;');
    })
})

describe('hideLoading function', function () {

    beforeEach(() => {
        setFixtures(`
        <div id="spinner-wrapper" style="visibility: visible;">
            <div id="spinner" Title="loading"></div>
        </div>
        `);
    });

    it('should set style to visibility: hidden on #spinner-wrapper', function () {
        hideLoading();
        expect($("#spinner-wrapper").attr('style')).toEqual('visibility: hidden;');
    })
})

// tests for functions in filters.js

describe('pages_fcn function', function() {
    it('should return an array with an object inside it', function() {
        let arr = ['A', 'B', 'C'];
        let n = 5;
        let result = pages_fcn(arr, n);
        expect(result).toEqual([{page1: ['A', 'B', 'C']}])
    })

    it('should return the input array split into chunks objects of 2', function() {
        let arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'];
        let n = 2;
        let result = pages_fcn(arr, n);
        expect(result).toEqual([
            { page1: [ 'A', 'B'] }, 
            { page2: [ 'C', 'D'] },
            { page3: [ 'E', 'F'] },
            { page4: [ 'G', 'H'] },
            { page5: [ 'I', 'J'] },
        ])
    })

    it('should return the input array split into chunks objects of 3', function() {
        let arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'];
        let n = 3;
        let result = pages_fcn(arr, n);
        expect(result).toEqual([
            { page1: [ 'A', 'B', 'C' ] }, 
            { page2: [ 'D', 'E', 'F' ] },
            { page3: [ 'G', 'H', 'I' ] },
            { page4: [ 'J' ] },
        ])
    })

    it('should return the input array split into chunks objects of 7', function() {
        let arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'];
        let n = 7;
        let result = pages_fcn(arr, n);
        expect(result).toEqual([
            { page1: [ 'A', 'B', 'C', 'D', 'E', 'F', 'G' ] }, 
            { page2: [ 'H', 'I', 'J' ] }
        ])
    })
})

describe('getCheckedIds function', function() {
    it('should return an empty array', function() {
        setFixtures(`
        <input class="mock-checkbox-js" name="A" type="checkbox" id="A">
        <input class="mock-checkbox-js" name="B" type="checkbox" id="B">
        <input class="mock-checkbox-js" name="C" type="checkbox" id="C">
        <input class="mock-checkbox-js" name="D" type="checkbox" id="D">
        <input class="mock-checkbox-js" name="E" type="checkbox" id="E">
        `);
        let checkboxes = $('.mock-checkbox-js');
        let result = getCheckedIds(checkboxes);
        expect(result).toEqual([])
    })
    it('should return array with ids A, C and E', function() {
        setFixtures(`
        <input class="mock-checkbox-js" name="A" type="checkbox" id="A" checked>
        <input class="mock-checkbox-js" name="B" type="checkbox" id="B">
        <input class="mock-checkbox-js" name="C" type="checkbox" id="C" checked>
        <input class="mock-checkbox-js" name="D" type="checkbox" id="D">
        <input class="mock-checkbox-js" name="E" type="checkbox" id="E" checked>
        `);
        let checkboxes = $('.mock-checkbox-js');
        let result = getCheckedIds(checkboxes);
        expect(result).toEqual(['A', 'C', 'E'])
    })
})