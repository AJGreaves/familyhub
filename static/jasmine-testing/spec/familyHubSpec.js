describe('alertModal function', function() {
    setFixtures(`
        <div id="alertModal">
            <h2 id="alertHeading"></h2>
            <p id="alertMessage"></p>
            <p id="alertMessageLine2"></p>
        </div>
        `);
    it('should add text "Sorry" to #alertHeading', function() {
        alertModal('no user match');
        expect($('#alertHeading').text()).toEqual('Sorry');
    });
})