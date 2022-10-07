$(function(){
    $(".alert-success").hide();
    $(".alert-danger").hide();

    var navbar = document.getElementById("navbar");
    var sticky = 1;

    window.onscroll = function() {
        if (window.pageYOffset >= sticky) {
            navbar.classList.add("sticky")
        } else {
            navbar.classList.remove("sticky");
        }
    };

    $('#contact-submit').on('click', function(e) {
        $('#contact-submit').css("color", "#")
    })

    $('#contact-form').on('submit', function(e){
        e.preventDefault();
        //Legit don't know what this jquery stuff does
        const contactForm = new FormData();
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        contactForm.append('name', $("#name-text").val());
        contactForm.append('email', $("#email-text").val());
        contactForm.append('message', $("#message-text").val());
        contactForm.append('csrfmiddlewaretoken', csrftoken);
        console.log(contactForm);
        fetch('', {
            method: 'POST',
            body: contactForm
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            $('#name-text').val('');
            $('#email-text').val('');
            $('#message-text').val('');
            $(".alert-success").first().hide().fadeIn(400).delay(5000).fadeOut(1000, function () { $(this).remove(); });
            // $(".alert-success").show('fade');
            // $(".alert-success").fadeTo(2000, 500).slideUp(500, function(){
            //     $(".alert-success").slideUp(500);
            // });
            // setTimeout(function () {
            //     $(".alert-success").hide('fade');
            // }, 7000)
        })
        .catch(error => {
            console.error('Error:', error);
            $('#name-text').val('');
            $('#email-text').val('');
            $('#message-text').val('');
            $(".alert-danger").first().hide().fadeIn(400).delay(5000).fadeOut(1000, function () { $(this).remove(); });
            // $(".alert-danger").show('fade');
            // $(".alert-danger").fadeTo(2000, 500).slideUp(500, function(){
            //     $(".alert-danger").slideUp(500);
            // });
            // setTimeout(function () {
            //     $(".alert-danger").hide('fade');
            // }, 7000)
        });
    });
});

