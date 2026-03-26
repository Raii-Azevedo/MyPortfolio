/*==================== toggle icon navbar ====================*/
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
};


/*==================== Navbar "active" effect while scrolling ====================*/
let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if (top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                let activeLink = document.querySelector('header nav a[href*=' + id + ']');
                if (activeLink) {
                    activeLink.classList.add('active');
                }
            });
        };
    });
    /*==================== Sticky Navbar ====================*/

    let header = document.querySelector('header');
    if (header) {
        header.classList.toggle('sticky', window.scrollY > 100);
    }

    /*==================== remove toggle icon and navbar when click navbar link (scroll) ====================*/
    if (menuIcon && navbar) {
        menuIcon.classList.remove('bx-x');
        navbar.classList.remove('active');
    }
};


/*==================== scroll reveal with error handling ====================*/
if (typeof ScrollReveal !== 'undefined') {
    ScrollReveal({
        distance: '80px',
        duration: 2000,
        delay: 200,
        reset: false // Set to false for better performance
    });

    ScrollReveal().reveal('.home-content, .heading', { origin: 'top' });
    ScrollReveal().reveal('.home-img, .services-container, .portfolio-box, .contact form', { origin: 'bottom' });
    ScrollReveal().reveal('.home-content h1, .about-img', { origin: 'left' });
    ScrollReveal().reveal('.home-content p, .about-content', { origin: 'right' });
}


/*==================== typed js with error handling ====================*/
if (typeof Typed !== 'undefined') {
    const typed = new Typed('.multiple-text', {
        strings: ['Fullstack Web Developer', 'Data Analyst', 'Blogger'],
        typeSpeed: 100,
        backSpeed: 100,
        backDelay: 1000,
        loop: true
    });
}


/*==================== ENHANCEMENTS ====================*/

/*==================== Smooth form validation and submission ====================*/
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    if (!contactForm) return; // Exit if form doesn't exist on page
    
    const submitBtn = document.getElementById('submitButton');
    const formStatus = document.createElement('div');
    formStatus.id = 'form-status';
    formStatus.className = 'alert';
    formStatus.style.display = 'none';
    contactForm.insertBefore(formStatus, contactForm.firstChild);
    
    // Create loader element
    const loader = document.createElement('span');
    loader.className = 'loader';
    loader.style.display = 'none';
    if (submitBtn) {
        submitBtn.parentNode.insertBefore(loader, submitBtn.nextSibling);
    }
    
    // Real-time validation for all required fields
    const requiredFields = contactForm.querySelectorAll('[required]');
    
    function validateField(field) {
        if (field.type === 'email') {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(field.value)) {
                field.setCustomValidity('Please enter a valid email address');
                field.classList.add('invalid');
                return false;
            } else {
                field.setCustomValidity('');
                field.classList.remove('invalid');
                return true;
            }
        } else if (field.type === 'tel') {
            const phoneRegex = /^[0-9]{10,11}$/;
            const cleanNumber = field.value.replace(/\D/g, '');
            if (!phoneRegex.test(cleanNumber)) {
                field.setCustomValidity('Please enter a valid phone number (10-11 digits)');
                field.classList.add('invalid');
                return false;
            } else {
                field.setCustomValidity('');
                field.classList.remove('invalid');
                return true;
            }
        } else if (field.value.trim() === '') {
            field.classList.add('invalid');
            return false;
        } else {
            field.classList.remove('invalid');
            return true;
        }
    }
    
    function validateForm() {
        if (!submitBtn) return;
        
        let isValid = true;
        requiredFields.forEach(field => {
            if (!validateField(field)) {
                isValid = false;
            }
        });
        submitBtn.disabled = !isValid;
        return isValid;
    }
    
    // Add event listeners to all required fields
    requiredFields.forEach(field => {
        field.addEventListener('input', function() {
            validateField(this);
            validateForm();
        });
        
        field.addEventListener('blur', function() {
            validateField(this);
            validateForm();
        });
    });
    
    // Form submission handler
    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            if (!validateForm()) {
                showStatus('Please fill all fields correctly.', 'danger');
                return;
            }
            
            if (submitBtn) submitBtn.disabled = true;
            if (loader) loader.style.display = 'inline-block';
            
            try {
                const formData = new FormData(contactForm);
                const response = await fetch(contactForm.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'Accept': 'application/json'
                    }
                });
                
                if (response.ok) {
                    showStatus('Message sent successfully! I\'ll get back to you soon.', 'success');
                    contactForm.reset();
                    validateForm();
                } else {
                    throw new Error('Form submission failed');
                }
            } catch (error) {
                console.error('Form submission error:', error);
                showStatus('Oops! Something went wrong. Please try again or email me directly at raissa@example.com.', 'danger');
            } finally {
                if (submitBtn) submitBtn.disabled = false;
                if (loader) loader.style.display = 'none';
                
                // Auto-hide status message after 5 seconds
                setTimeout(() => {
                    if (formStatus) formStatus.style.display = 'none';
                }, 5000);
            }
        });
    }
    
    function showStatus(message, type) {
        if (!formStatus) return;
        
        formStatus.textContent = message;
        formStatus.className = `alert alert-${type}`;
        formStatus.style.display = 'block';
        
        // Scroll to status message
        formStatus.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
    
    // Initial validation
    validateForm();
});


/*==================== Lazy loading images ====================*/
document.addEventListener('DOMContentLoaded', function() {
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src || img.src;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img[loading="lazy"]').forEach(img => {
            imageObserver.observe(img);
        });
    }
});


/*==================== Smooth scroll for anchor links ====================*/
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#' || href === '') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Update URL without jumping
                history.pushState(null, null, href);
            }
        });
    });
});


/*==================== Add active class to current section with better performance ====================*/
let ticking = false;

window.addEventListener('scroll', () => {
    if (!ticking) {
        requestAnimationFrame(() => {
            sections.forEach(sec => {
                let top = window.scrollY;
                let offset = sec.offsetTop - 150;
                let height = sec.offsetHeight;
                let id = sec.getAttribute('id');
                
                if (top >= offset && top < offset + height) {
                    navLinks.forEach(links => {
                        links.classList.remove('active');
                        let activeLink = document.querySelector(`header nav a[href*="${id}"]`);
                        if (activeLink) {
                            activeLink.classList.add('active');
                        }
                    });
                }
            });
            ticking = false;
        });
        ticking = true;
    }
});


/*==================== Handle portfolio image errors ====================*/
document.addEventListener('DOMContentLoaded', function() {
    const portfolioImages = document.querySelectorAll('.portfolio-box img');
    const placeholderImage = '/static/images/placeholder.jpg'; // Update with your placeholder path
    
    portfolioImages.forEach(img => {
        img.addEventListener('error', function() {
            this.src = placeholderImage;
            this.alt = 'Image not available';
        });
    });
});


/*==================== Add keyboard navigation support ====================*/
document.addEventListener('keydown', function(e) {
    // Close mobile menu with Escape key
    if (e.key === 'Escape' && navbar && navbar.classList.contains('active')) {
        menuIcon.classList.remove('bx-x');
        navbar.classList.remove('active');
    }
});


/*==================== Performance: Debounce resize events ====================*/
let resizeTimeout;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
        // Recalculate any dynamic layouts if needed
        if (window.innerWidth > 768 && navbar && navbar.classList.contains('active')) {
            menuIcon.classList.remove('bx-x');
            navbar.classList.remove('active');
        }
    }, 250);
});
