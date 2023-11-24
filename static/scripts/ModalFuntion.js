const buttons = document.querySelectorAll('button[data-bs-toggle="modal"]');
buttons.forEach(button => {
    button.addEventListener('click', () => {
        const dataId = button.getAttribute('data-bs-id');
        console.log(dataId);
        const myInput = document.querySelector('#password_id');
        myInput.value = dataId;
    });
});



