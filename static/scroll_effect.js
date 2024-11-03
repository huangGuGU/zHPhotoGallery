document.addEventListener('DOMContentLoaded', function() {
    const textBlocks = document.querySelectorAll('.text-block');
    const imageBlocks = document.querySelectorAll('.image-block img');

    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top < window.innerHeight && rect.bottom > 0
        );
    }

    function checkVisibility() {
        textBlocks.forEach(function(block) {
            if (isInViewport(block) && !block.classList.contains('visible')) {
                block.classList.add('visible');
            }
        });

        imageBlocks.forEach(function(img) {
            if (isInViewport(img) && !img.classList.contains('visible')) {
                img.classList.add('visible');
            }
        });
    }

    window.addEventListener('scroll', checkVisibility);
    checkVisibility(); // 页面加载时检查一次
});