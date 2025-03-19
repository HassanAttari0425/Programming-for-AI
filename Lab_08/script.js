document.addEventListener("DOMContentLoaded", function () {
    const themeButton = document.getElementById("changeTheme");

    // Toggle dark mode
    themeButton.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");
    });

    // Print title in console for debugging
    console.log("NASA APOD Title:", document.getElementById("title").innerText);
});
