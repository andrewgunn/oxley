(function () {
  var doc = document.documentElement;
  doc.classList.remove('no-js');

  // Header shadow + mobile action bar once the user scrolls
  var header = document.querySelector('.header');
  var bar = document.querySelector('.mobile-bar');
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle('is-scrolled', y > 8);
    if (bar) bar.classList.toggle('is-visible', y > 420);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile drawer
  var drawer = document.getElementById('drawer');
  var openBtn = document.querySelector('[data-drawer-open]');
  var lastFocus;
  function setDrawer(open) {
    if (!drawer) return;
    drawer.classList.toggle('is-open', open);
    drawer.setAttribute('aria-hidden', String(!open));
    if (openBtn) openBtn.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
    if (open) {
      lastFocus = document.activeElement;
      var first = drawer.querySelector('button, a');
      if (first) first.focus();
    } else if (lastFocus) {
      lastFocus.focus();
    }
  }
  if (openBtn) openBtn.addEventListener('click', function () { setDrawer(true); });
  document.querySelectorAll('[data-drawer-close]').forEach(function (el) {
    el.addEventListener('click', function () { setDrawer(false); });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      setDrawer(false);
      document.querySelectorAll('.nav__item.is-open').forEach(function (i) { i.classList.remove('is-open'); });
    }
  });

  // Desktop dropdown: click/keyboard support (hover handled in CSS)
  document.querySelectorAll('.nav__toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.nav__item');
      var open = !item.classList.contains('is-open');
      item.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', String(open));
    });
  });
  document.addEventListener('click', function (e) {
    document.querySelectorAll('.nav__item.is-open').forEach(function (item) {
      if (!item.contains(e.target)) {
        item.classList.remove('is-open');
        item.querySelector('.nav__toggle').setAttribute('aria-expanded', 'false');
      }
    });
  });

  // Reveal on scroll
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  }

  // Enquiry form: this static preview has no backend, so compose an email instead.
  // On go-live, point the form's action at the real form handler and remove this.
  document.querySelectorAll('form[data-enquiry]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var d = new FormData(form);
      var lines = [
        'Name: ' + d.get('name'),
        'Email: ' + d.get('email'),
        'Phone: ' + d.get('phone'),
        'Preferred contact: ' + (d.get('method') || '-'),
        'Help with: ' + (d.get('topic') || '-'),
        'Newsletter: ' + (d.get('newsletter') ? 'Yes' : 'No'),
        '',
        d.get('message') || ''
      ];
      var href = 'mailto:hello@oxleymortgages.co.uk'
        + '?subject=' + encodeURIComponent('Mortgage enquiry from ' + d.get('name'))
        + '&body=' + encodeURIComponent(lines.join('\n'));
      window.location.href = href;
      var status = form.querySelector('.form__status');
      if (status) status.textContent = 'Opening your email app — just press send and we’ll be in touch.';
    });
  });

  var year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();
})();
