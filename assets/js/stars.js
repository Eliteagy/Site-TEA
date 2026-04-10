/* ========== STARRY BACKGROUND GENERATOR ========== */
(function() {
    const initStars = () => {
        const container = document.getElementById('starryBg');
        if (!container) return;
        
        // Clear if already populated to avoid duplicate stars
        container.innerHTML = '';

        const starCount = 180; // Slightly more for a richer feel
        const fragment = document.createDocumentFragment();

        for (let i = 0; i < starCount; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            
            // Random position (%)
            const x = Math.random() * 100;
            const y = Math.random() * 100;
            
            // Random size (0.5px to 2.5px)
            const size = Math.random() * 1.8 + 0.6;
            
            // Random animation settings
            const duration = Math.random() * 3 + 3; // 3-6s twinkle
            const delay = Math.random() * 10;
            
            // Random drift direction and duration
            // This creates a slow, random movement for each star
            const driftX = (Math.random() - 0.5) * 40; // -20 to 20px
            const driftY = (Math.random() - 0.5) * 40; // -20 to 20px
            const driftDuration = Math.random() * 20 + 40; // 40-60s drift (very slow)
            
            star.style.left = `${x}%`;
            star.style.top = `${y}%`;
            star.style.width = `${size}px`;
            star.style.height = `${size}px`;
            
            star.style.setProperty('--duration', `${duration}s`);
            star.style.setProperty('--delay', `-${delay}s`); // Negative delay to start mid-animation
            star.style.setProperty('--drift-x', `${driftX}px`);
            star.style.setProperty('--drift-y', `${driftY}px`);
            star.style.setProperty('--drift-duration', `${driftDuration}s`);
            
            fragment.appendChild(star);
        }
        
        container.appendChild(fragment);
    };

    // Initialize on DOM load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initStars);
    } else {
        initStars();
    }
})();
