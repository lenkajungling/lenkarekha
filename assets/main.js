// Mobilní menu
(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.querySelector('.nav');
  if (!btn || !nav) return;
  btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.textContent = open ? 'Zavřít' : 'Menu';
  });
})();

// Filtr rozvrhu podle místa
(function () {
  var buttons = document.querySelectorAll('.filters button');
  if (!buttons.length) return;
  buttons.forEach(function (b) {
    b.addEventListener('click', function () {
      var city = b.getAttribute('data-city');
      buttons.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      document.querySelectorAll('tr[data-city]').forEach(function (row) {
        row.hidden = city !== 'vse' && row.getAttribute('data-city') !== city;
      });
    });
  });
})();

// Formuláře přes Formspree bez opuštění stránky
(function () {
  document.querySelectorAll('form[data-ajax]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = form.querySelector('.form-status');
      var submit = form.querySelector('[type="submit"]');
      status.className = 'form-status';
      status.textContent = 'Odesílám…';
      submit.disabled = true;
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
        .then(function (r) {
          if (!r.ok) throw new Error('bad status');
          form.reset();
          status.className = 'form-status ok';
          status.textContent = 'Děkuju, zpráva dorazila. Ozvu se ti obvykle do 24 hodin.';
        })
        .catch(function () {
          status.className = 'form-status err';
          status.textContent = 'Zprávu se nepodařilo odeslat. Zkus to prosím znovu, nebo mi napiš přímo na e-mail či WhatsApp.';
        })
        .finally(function () { submit.disabled = false; });
    });
  });
})();

// Jemný pohyb fotek při posouvání (parallax)
(function () {
  var imgs = Array.prototype.slice.call(document.querySelectorAll('[data-parallax]'));
  if (!imgs.length || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var ticking = false;
  function update() {
    var vh = window.innerHeight;
    imgs.forEach(function (img) {
      var r = img.parentNode.parentNode.getBoundingClientRect();
      if (r.bottom < -100 || r.top > vh + 100) return;
      var shift = ((r.top + r.height / 2) - vh / 2) * -0.12;
      img.style.transform = 'translate3d(0,' + shift.toFixed(1) + 'px,0)';
    });
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  window.addEventListener('resize', update);
  update();
})();

// Hloubkoměr: čím níž na stránce, tím hlouběji (dno = 40 m, hloubka AIDA4)
(function () {
  var val = document.querySelector('.depth-val');
  var dot = document.querySelector('.depth-dot');
  if (!val) return;
  function update() {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var f = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 0;
    val.textContent = '−' + Math.round(f * 40) + ' m';
    dot.style.top = (f * 133) + 'px';
  }
  window.addEventListener('scroll', update, { passive: true });
  update();
})();

// Obsah pod okrajem obrazovky při posouvání „vyplave“
(function () {
  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var els = document.querySelectorAll('[data-rv]');
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (el) {
    if (el.getBoundingClientRect().top > window.innerHeight) { el.classList.add('rv'); io.observe(el); }
  });
})();

// Reference: posun pásu šipkami
(function () {
  document.querySelectorAll('.ref-slider').forEach(function (slider) {
    var track = slider.querySelector('.ref-track');
    function step(dir) {
      var card = track.querySelector('.ref-card');
      var w = card ? card.getBoundingClientRect().width + 18 : 320;
      track.scrollBy({ left: dir * w, behavior: 'smooth' });
    }
    slider.querySelector('.ref-prev').addEventListener('click', function () { step(-1); });
    slider.querySelector('.ref-next').addEventListener('click', function () { step(1); });
  });
})();
