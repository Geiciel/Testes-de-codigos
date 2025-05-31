document.addEventListener("DOMContentLoaded", function() {
    const burger = document.getElementById("burger");
    const nav = document.querySelector(".nav");

    burger.onclick = function() {
        // Alterna a exibição do menu
        if (nav.style.display === "flex") {
            nav.style.display = "none";
        } else {
            nav.style.display = "flex";
        }
    };
});