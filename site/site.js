(() => {
  const checkout = document.querySelector('[data-checkout-url]');
  if (!checkout) return;
  const url = checkout.dataset.checkoutUrl.trim();
  if (!url) return;
  const link = document.createElement('a');
  link.className = 'button button-primary';
  link.href = url;
  link.textContent = 'Get the full kit ↗';
  link.target = '_blank';
  link.rel = 'noopener';
  checkout.replaceWith(link);
})();
