const menuIcon = document.querySelector('#menu-icon');
const navbar = document.querySelector('.navbar');
const header = document.querySelector('.header');
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('header nav a');

if (menuIcon && navbar) {
    menuIcon.addEventListener('click', () => {
        menuIcon.classList.toggle('bx-x');
        navbar.classList.toggle('active');
    });
}

const updateNavigation = () => {
    const scrollY = window.scrollY;

    if (header) {
        header.classList.toggle('sticky', scrollY > 40);
    }

    sections.forEach((section) => {
        const offset = section.offsetTop - 180;
        const height = section.offsetHeight;
        const id = section.getAttribute('id');

        if (scrollY >= offset && scrollY < offset + height) {
            navLinks.forEach((link) => link.classList.remove('active'));
            const activeLink = document.querySelector(`header nav a[href="#${id}"]`);
            if (activeLink) activeLink.classList.add('active');
        }
    });
};

window.addEventListener('scroll', updateNavigation);
window.addEventListener('load', updateNavigation);

document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (!target) return;

        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });

        if (navbar && menuIcon) {
            navbar.classList.remove('active');
            menuIcon.classList.remove('bx-x');
        }
    });
});

if (typeof ScrollReveal !== 'undefined') {
    const sr = ScrollReveal({
        distance: '60px',
        duration: 1200,
        delay: 100,
        reset: false
    });

    sr.reveal('.home-content, .section-kicker, .heading', { origin: 'top' });
    sr.reveal('.terminal-block, .services-box, .portfolio-box, .contact form', { origin: 'bottom', interval: 100 });
    sr.reveal('.about-img-wrap', { origin: 'left' });
    sr.reveal('.about-content', { origin: 'right' });
}

if (typeof Typed !== 'undefined') {
    new Typed('.multiple-text', {
        strings: [
            'Analytics Engineer',
            'Data Developer',
            'Pipeline Builder',
            'Dashboard Creator',
            'SQL Specialist',
        ],
        typeSpeed: 60,
        backSpeed: 35,
        backDelay: 1400,
        loop: true
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contactForm');
    if (!contactForm) return;

    const submitBtn = document.getElementById('submitButton');
    const formStatus = document.createElement('div');
    formStatus.id = 'form-status';
    formStatus.className = 'alert';
    formStatus.style.display = 'none';
    contactForm.prepend(formStatus);

    const loader = document.createElement('span');
    loader.className = 'loader';
    loader.style.display = 'none';
    submitBtn?.insertAdjacentElement('afterend', loader);

    const requiredFields = contactForm.querySelectorAll('[required]');

    const validateField = (field) => {
        const value = field.value.trim();

        if (field.type === 'email') {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            const isValid = emailRegex.test(value);
            field.classList.toggle('invalid', !isValid);
            field.setCustomValidity(isValid ? '' : 'Please enter a valid email address.');
            return isValid;
        }

        if (field.type === 'tel') {
            const cleanValue = value.replace(/\D/g, '');
            const isValid = cleanValue.length >= 8 && cleanValue.length <= 15;
            field.classList.toggle('invalid', !isValid);
            field.setCustomValidity(isValid ? '' : 'Please enter a valid phone number.');
            return isValid;
        }

        const isValid = value.length > 0;
        field.classList.toggle('invalid', !isValid);
        field.setCustomValidity(isValid ? '' : 'This field is required.');
        return isValid;
    };

    const validateForm = () => {
        let isValid = true;
        requiredFields.forEach((field) => {
            if (!validateField(field)) isValid = false;
        });
        if (submitBtn) submitBtn.disabled = !isValid;
        return isValid;
    };

    requiredFields.forEach((field) => {
        field.addEventListener('input', () => validateForm());
        field.addEventListener('blur', () => validateForm());
    });

    const showStatus = (message, type) => {
        formStatus.textContent = message;
        formStatus.className = `alert alert-${type}`;
        formStatus.style.display = 'block';
    };

    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        if (!validateForm()) {
            showStatus('Please fill out all fields correctly.', 'danger');
            return;
        }

        if (submitBtn) submitBtn.disabled = true;
        loader.style.display = 'inline-block';

        try {
            const response = await fetch(contactForm.action, {
                method: 'POST',
                body: new FormData(contactForm),
                headers: { Accept: 'application/json' }
            });

            if (!response.ok) throw new Error('Failed to submit');

            showStatus("Message sent successfully! I'll get back to you soon.", 'success');
            contactForm.reset();
            validateForm();
        } catch (error) {
            showStatus('Something went wrong. Please try again in a moment.', 'danger');
        } finally {
            if (submitBtn) submitBtn.disabled = false;
            loader.style.display = 'none';
            setTimeout(() => {
                formStatus.style.display = 'none';
            }, 5000);
        }
    });

    document.querySelectorAll('.portfolio-box img').forEach((img) => {
        img.addEventListener('error', () => {
            img.src = '/static/images/home.png';
        });
    });

    validateForm();
});
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
      