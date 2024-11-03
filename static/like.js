document.addEventListener('DOMContentLoaded', function() {
    // 选择所有点赞图标
    const icons = document.querySelectorAll('.like-icon');

    icons.forEach(icon => {
        icon.addEventListener('click', function() {
            // 获取图片名称
            const imageName = icon.getAttribute('data-image');

            // 发送 POST 请求到 /like_image 路由
            fetch(`/like_image`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ image: imageName })
            })
            .then(response => response.json())
            .then(data => {
                // 更新点赞计数
                const likeCountElement = document.getElementById(`like-count-${imageName}`);
                likeCountElement.textContent = data.likes;
            })
            .catch(error => console.error('Error:', error));
        });
    });
});