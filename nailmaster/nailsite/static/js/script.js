document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('exampleModal');
    const images = document.querySelectorAll('.images');
    const carouselElement = document.getElementById('carouselExample');
    const carousel = new bootstrap.Carousel(carouselElement, {
        interval: false
    });

    images.forEach(img => {
        img.addEventListener('click', function () {
            const index = this.getAttribute('data-index');
            carousel.to(index);
        });
    });
});