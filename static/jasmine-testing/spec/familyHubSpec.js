describe('alertModal function', function() {
    beforeEach(() => {
        setFixtures(`
            <div id="alertModal">
                <h2 id="alertHeading"></h2>
                <p id="alertMessage"></p>
                <p id="alertMessageLine2"></p>
            </div>
            `);
    });    
    it('should add text "Sorry" to #alertHeading', function() {
        alertModal('no user match');
        expect($('#alertHeading').text()).toEqual('Sorry');
    });
    it('should add text "No account with this username or email address.\n Please try again." to #alertMessage', function() {
        alertModal('no user match');
        expect($('#alertMessage').text()).toEqual('No account with this username or email address.\n Please try again.');
    });
    it('should add text "Error" to #alertHeading', function() {
        alertModal('start end dates wrong', '02/01/2019', '01/01/2019');
        expect($('#alertHeading').text()).toEqual('Error');
    });
    it('should add text "You input a finish date 01/01/2019" to #alertMessage', function() {
        alertModal('start end dates wrong', '02/01/2019', '01/01/2019');
        expect($('#alertMessage').text()).toEqual('You input a finish date 01/01/2019');
    });
    it('should add text "that is before your start date 02/01/2019" to #alertMessageLine2', function() {
        alertModal('start end dates wrong', '02/01/2019', '01/01/2019');
        expect($('#alertMessageLine2').text()).toEqual('that is before your start date 02/01/2019');
    });
    it('should add text "Sorry" to #alertHeading', function() {
        alertModal('no share');
        expect($('#alertHeading').text()).toEqual('Sorry');
    });
    it("should add text You can't share this page in preview mode. to #alertMessage", function() {
        alertModal('no share');
        expect($('#alertMessage').text()).toEqual("You can't share this page in preview mode.");
    });
    it('should add text "Once you have published it, the share links will work" to #alertMessageLine2', function() {
        alertModal('no share');
        expect($('#alertMessageLine2').text()).toEqual('Once you have published it, the share links will work');
    });
    it('should toggle .active class onto #alertModal', function() {
        alertModal('');
        expect($('#alertModal')).toHaveClass('active');
    })
})

describe('openLoggedInModal function', function() {
    beforeEach(() => {
        setFixtures(`
        <div id="loggedInModal">
            <h2 id="welcomeMessage"></h2>
            <a id="accountUrl" href="#">My listings</a>
            <a id="newActivityUrl" href="#">Add new activity</a>
        </div>
        `);
    }); 
    it('should add welcome message that includes username', function() {
        openLoggedInModal('Arthur Dent');
        expect($('#welcomeMessage').text()).toEqual('Welcome Arthur Dent.')
    });
    it('should create account page href url that includes username', function() {
        openLoggedInModal('Zaphod Beeblebrox');
        expect($("#accountUrl").attr('href')).toEqual('/account/zaphod-beeblebrox');
    });
    it('should create editor page href url that includes username', function() {
        openLoggedInModal('Slartibartfast');
        expect($("#newActivityUrl").attr('href')).toEqual('/editor/slartibartfast/add-new');
    });
    it('should add .active class to #loggedInModal', function() {
        openLoggedInModal('');
        expect($('#loggedInModal')).toHaveClass('active');
    })
})
