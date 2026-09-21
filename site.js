(() => {
  const checkout = document.querySelector('[data-checkout-url]');
  if (!checkout) return;
  const url = checkout.dataset.checkoutUrl.trim();
  if (url) {
    checkout.href = url;
    checkout.textContent = 'Get the full kit ↗';
    checkout.classList.remove('button-disabled');
    checkout.removeAttribute('aria-disabled');
    checkout.target = '_blank';
    checkout.rel = 'noopener';
  }
})();
