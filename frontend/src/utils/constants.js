export const PLATFORMS = [
  { id: 'amazon', name: 'Amazon', color: '#FF9900' },
  { id: 'flipkart', name: 'Flipkart', color: '#1f42e9' },
  { id: 'myntra', name: 'Myntra', color: '#ffc41e' },
  { id: 'ajio', name: 'Ajio', color: '#1f42e9' },
  { id: 'croma', name: 'Croma', color: '#e00000' },
];

export const formatPrice = (price) => {
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
  }).format(price);
};

export const calculateDiscount = (originalPrice, currentPrice) => {
  return Math.round(((originalPrice - currentPrice) / originalPrice) * 100);
};
