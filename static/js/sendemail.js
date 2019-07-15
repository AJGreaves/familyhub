$(document).ready(function () {

    if (document.querySelector('#contact-form')) {

        const contactForm = document.querySelector('#contact-form');

        contactForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const data = {
                service_id: "gmail",
                template_id: "familyhub_contact_form",
                user_id: "user_CQSk7h9Wyuw2xLhYG0hBX",
                template_params: {
                    "from_name": contactForm.contactName.value,
                    "from_email": contactForm.contactEmail.value,
                    "subject": contactForm.contactSubject.value,
                    "contact_form_message": contactForm.contactMessage.value,
                }
            };

            $.ajax('https://api.emailjs.com/api/v1.0/email/send', {
                type: 'POST',
                data: JSON.stringify(data),
                contentType: 'application/json'
            }).done(function () {
                $('input').val('');
                $('textarea').val('');
                alertModal('email sent');
            }).fail(function (error) {
                console.log('Oops... ' + JSON.stringify(error));
                alertModal('error');
            });
        });

    }

    if (document.querySelector('#email-activity-form')) {

        const emailActivityForm = document.querySelector('#email-activity-form');

        emailActivityForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const data = {
                service_id: "gmail",
                template_id: "template_idQ1AXyu",
                user_id: "user_CQSk7h9Wyuw2xLhYG0hBX",
                template_params: {
                    "company_to_email": emailActivityForm.emailActivityTo.value,
                    "from_name": emailActivityForm.emailActivityFromName.value,
                    "from_email": emailActivityForm.emailActivityFromEmail.value,
                    "message": emailActivityForm.emailActivityMessage.value,
                }
            };

            $.ajax('https://api.emailjs.com/api/v1.0/email/send', {
                type: 'POST',
                data: JSON.stringify(data),
                contentType: 'application/json'
            }).done(function () {
                $('#emailActivityModal').modal('hide');
                alertModal('business email sent');
            }).fail(function (error) {
                console.log('Oops... ' + JSON.stringify(error));
                alertModal('error');
            });
        });

        $('#emailOrganisers').click(function() {
            alert("Although this is a student project, the email forms on listing pages are wired up to real business's email addresses. Therefore if you wish to test this function please make sure you are testing it in a listing you created with your own email address in. Thank you!");
        });

    }
});