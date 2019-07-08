
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