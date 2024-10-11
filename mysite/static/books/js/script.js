document.addEventListener('DOMContentLoaded', function () {


    const links = document.querySelectorAll('.nav-link');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            links.forEach(link => link.classList.remove('active'));
            this.classList.add('active');
            console.log(this.text)
        });
    });


    const spans = document.querySelectorAll('span');
    spans.forEach(span => span.classList.add('d-block'));

    const labels = document.querySelectorAll('label');
    labels.forEach(label => label.classList.add('form-label'));

    const inputs = document.querySelectorAll('input');
    inputs.forEach(input => input.classList.add('form-control','mb-3'));

    const errors = document.getElementsByClassName('errorlist');
    Array.from(errors).forEach(error => {
        error.style.color = 'red';
        error.style.fontWeight = 'bold';
    });

    const select = document.querySelector('select');
    if (select) {
        select.classList.add('form-control');
    }

    const divs = document.getElementsByClassName('form_element');
    Array.from(divs).forEach(div => div.classList.add('mb-3'));

    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => checkbox.classList.remove('form-control'));

    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => textarea.classList.add('form-control'));
});








