// Interactive JavaScript for Mini Cart

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all interactive features
    initScrollAnimations();
    initSmoothScrolling();
    initCarouselEnhancements();
    initModalEnhancements();
    initFormEnhancements();
    initLoadingAnimations();
    initHoverEffects();
});

// Scroll Animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
            }
        });
    }, observerOptions);

    // Add scroll-reveal class to elements that should animate on scroll
    const elementsToAnimate = document.querySelectorAll('.popular-card, .popular-card-lap, .card.mb-3, .border.rounded.p-2, .sec2, .w3-ios-background');
    elementsToAnimate.forEach(el => {
        el.classList.add('scroll-reveal');
        observer.observe(el);
    });
}

// Smooth Scrolling
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Carousel Enhancements
function initCarouselEnhancements() {
    const carousels = document.querySelectorAll('.carousel');
    carousels.forEach(carousel => {
        // Add pause on hover
        carousel.addEventListener('mouseenter', () => {
            const bsCarousel = new bootstrap.Carousel(carousel);
            bsCarousel.pause();
        });
        carousel.addEventListener('mouseleave', () => {
            const bsCarousel = new bootstrap.Carousel(carousel);
            bsCarousel.cycle();
        });

        // Add touch/swipe support for mobile
        let startX = 0;
        let endX = 0;

        carousel.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
        });

        carousel.addEventListener('touchend', (e) => {
            endX = e.changedTouches[0].clientX;
            handleSwipe(carousel, startX, endX);
        });
    });
}

function handleSwipe(carousel, startX, endX) {
    const threshold = 50;
    if (startX - endX > threshold) {
        // Swipe left - next slide
        const bsCarousel = new bootstrap.Carousel(carousel);
        bsCarousel.next();
    } else if (endX - startX > threshold) {
        // Swipe right - previous slide
        const bsCarousel = new bootstrap.Carousel(carousel);
        bsCarousel.prev();
    }
}

// Modal Enhancements
function initModalEnhancements() {
    const modals = document.querySelectorAll('.w3-modal');
    modals.forEach(modal => {
        // Close modal when clicking outside
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                modal.style.display = 'none';
            }
        });

        // Add escape key support
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && modal.style.display === 'block') {
                modal.style.display = 'none';
            }
        });
    });

    // Add modal open animations
    const modalContents = document.querySelectorAll('.w3-modal-content');
    modalContents.forEach(content => {
        content.style.animation = 'modalFadeIn 0.3s ease-out';
    });
}

// Form Enhancements
function initFormEnhancements() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea');
        inputs.forEach(input => {
            // Add floating label effect
            input.addEventListener('focus', function() {
                this.parentElement.classList.add('focused');
            });
            input.addEventListener('blur', function() {
                if (!this.value) {
                    this.parentElement.classList.remove('focused');
                }
            });

            // Real-time validation feedback
            input.addEventListener('input', function() {
                validateInput(this);
            });
        });

        // Enhance form submission
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting...';
                submitBtn.disabled = true;
            }
        });
    });
}

function validateInput(input) {
    const value = input.value.trim();
    const isValid = value !== '';

    input.classList.toggle('is-valid', isValid);
    input.classList.toggle('is-invalid', !isValid && input.hasAttribute('required'));
}

// Loading Animations
function initLoadingAnimations() {
    // Add loading class to body initially
    document.body.classList.add('loading');

    // Remove loading class after page load
    window.addEventListener('load', function() {
        document.body.classList.remove('loading');
        document.body.classList.add('loaded');
    });

    // Add loading animation to images
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        img.addEventListener('load', function() {
            this.classList.add('loaded');
        });
    });
}

// Hover Effects
function initHoverEffects() {
    // Add ripple effect to buttons
    const buttons = document.querySelectorAll('.btn, .w3-button');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');
            this.appendChild(ripple);

            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = e.clientX - rect.left - size / 2 + 'px';
            ripple.style.top = e.clientY - rect.top - size / 2 + 'px';

            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });

    // Add tooltip functionality
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    tooltipElements.forEach(el => {
        el.addEventListener('mouseenter', showTooltip);
        el.addEventListener('mouseleave', hideTooltip);
    });
}

function showTooltip(e) {
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.textContent = e.target.getAttribute('data-tooltip');
    document.body.appendChild(tooltip);

    const rect = e.target.getBoundingClientRect();
    tooltip.style.left = rect.left + rect.width / 2 - tooltip.offsetWidth / 2 + 'px';
    tooltip.style.top = rect.top - tooltip.offsetHeight - 5 + 'px';
}

function hideTooltip() {
    const tooltips = document.querySelectorAll('.tooltip');
    tooltips.forEach(tooltip => tooltip.remove());
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Add CSS for additional interactive elements
const style = document.createElement('style');
style.textContent = `
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.6);
        transform: scale(0);
        animation: ripple 0.6s linear;
        pointer-events: none;
    }

    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }

    .tooltip {
        position: absolute;
        background: rgba(0, 0, 0, 0.8);
        color: white;
        padding: 5px 10px;
        border-radius: 4px;
        font-size: 12px;
        white-space: nowrap;
        z-index: 1000;
        pointer-events: none;
    }

    .is-valid {
        border-color: #28a745 !important;
        box-shadow: 0 0 0 0.2rem rgba(40, 167, 69, 0.25);
    }

    .is-invalid {
        border-color: #dc3545 !important;
        box-shadow: 0 0 0 0.2rem rgba(220, 53, 69, 0.25);
    }

    @keyframes modalFadeIn {
        from {
            opacity: 0;
            transform: scale(0.9) translateY(-20px);
        }
        to {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
    }

    .loading {
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .loaded {
        opacity: 1;
    }

    img {
        transition: opacity 0.3s ease;
    }

    img.loaded {
        opacity: 1;
    }

    img:not(.loaded) {
        opacity: 0;
    }
`;
document.head.appendChild(style);

// Add some accessibility improvements
function initAccessibility() {
    // Add ARIA labels where missing
    const buttons = document.querySelectorAll('button:not([aria-label])');
    buttons.forEach(btn => {
        if (btn.textContent.trim()) {
            btn.setAttribute('aria-label', btn.textContent.trim());
        }
    });

    // Improve keyboard navigation
    const focusableElements = document.querySelectorAll('a, button, input, select, textarea');
    focusableElements.forEach(el => {
        el.addEventListener('focus', function() {
            this.style.outline = '2px solid #667eea';
        });
        el.addEventListener('blur', function() {
            this.style.outline = '';
        });
    });
}

// Initialize accessibility features
initAccessibility();
