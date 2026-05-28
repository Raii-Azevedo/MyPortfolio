const menuIcon = document.querySelector('#menu-icon');
const navbar = document.querySelector('.navbar');
const header = document.querySelector('.header');
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('header nav a');

/* ── mobile menu ── */
if (menuIcon && navbar) {
    menuIcon.addEventListener('click', () => {
        menuIcon.classList.toggle('bx-x');
        navbar.classList.toggle('active');
    });
}

/* ── sticky header + active nav link ── */
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

/* ── smooth scroll ── */
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

/* ── scroll reveal ── */
if (typeof ScrollReveal !== 'undefined') {
    const sr = ScrollReveal({
        distance: '50px',
        duration: 1000,
        delay: 100,
        reset: false
    });

    sr.reveal('.home-content, .section-kicker, .heading', { origin: 'top' });
    sr.reveal('.terminal-block, .services-box, .portfolio-box, .contact form', { origin: 'bottom', interval: 100 });
    sr.reveal('.about-content', { origin: 'bottom' });
}

/* ── typed.js ── */
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

/* ── contact form ── */
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
    if (submitBtn) submitBtn.insertAdjacentElement('afterend', loader);

    const requiredFields = contactForm.querySelectorAll('[required]');

    const validateField = (field) => {
        const value = field.value.trim();

        if (field.type === 'email') {
            const isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
            field.classList.toggle('invalid', !isValid);
            field.setCustomValidity(isValid ? '' : 'Please enter a valid email address.');
            return isValid;
        }

        if (field.type === 'tel') {
            const clean = value.replace(/\D/g, '');
            const isValid = clean.length >= 8 && clean.length <= 15;
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
        requiredFields.forEach((field) => { if (!validateField(field)) isValid = false; });
        if (submitBtn) submitBtn.disabled = !isValid;
        return isValid;
    };

    requiredFields.forEach((field) => {
        field.addEventListener('input', validateForm);
        field.addEventListener('blur', validateForm);
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
        } catch {
            showStatus('Something went wrong. Please try again in a moment.', 'danger');
        } finally {
            if (submitBtn) submitBtn.disabled = false;
            loader.style.display = 'none';
            setTimeout(() => { formStatus.style.display = 'none'; }, 5000);
        }
    });

    validateForm();
});

/* ── keyboard nav ── */
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navbar && navbar.classList.contains('active')) {
        menuIcon.classList.remove('bx-x');
        navbar.classList.remove('active');
    }
});

/* ── resize debounce ── */
let resizeTimeout;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
        if (window.innerWidth > 768 && navbar && navbar.classList.contains('active')) {
            menuIcon.classList.remove('bx-x');
            navbar.classList.remove('active');
        }
    }, 250);
});
