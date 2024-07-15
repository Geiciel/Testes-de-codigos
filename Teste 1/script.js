document.addEventListener("DOMContentLoaded", () => {
    // Exemplo 1: Mudar cor do botão ao clicar
    const button = document.querySelector('.button');
    button.addEventListener('click', () => {
        button.classList.toggle('clicked');
    });

    // Exemplo 4: Mudar cor dos itens da lista ao clicar
    const listItems = document.querySelectorAll('.list-item');
    listItems.forEach(item => {
        item.addEventListener('click', () => {
            item.classList.toggle('clicked');
        });
    });
});
