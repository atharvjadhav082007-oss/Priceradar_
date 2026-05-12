import apiClient from './apiClient';

export const searchProducts = async (query, platforms = []) => {
  try {
    const response = await apiClient.get('/products/search', {
      params: { q: query, platforms: platforms.join(',') }
    });
    return response.data;
  } catch (error) {
    console.error('Search error:', error);
    throw error;
  }
};

export const getProductDetails = async (productId) => {
  try {
    const response = await apiClient.get(`/products/${productId}`);
    return response.data;
  } catch (error) {
    console.error('Fetch product error:', error);
    throw error;
  }
};

export const getPriceHistory = async (productId) => {
  try {
    const response = await apiClient.get(`/products/${productId}/prices`);
    return response.data;
  } catch (error) {
    console.error('Fetch price history error:', error);
    throw error;
  }
};

export const comparePrices = async (productId) => {
  try {
    const response = await apiClient.get(`/compare/${productId}`);
    return response.data;
  } catch (error) {
    console.error('Compare prices error:', error);
    throw error;
  }
};

export const createAlert = async (productId, targetPrice) => {
  try {
    const response = await apiClient.post('/alerts', {
      product_id: productId,
      target_price: targetPrice
    });
    return response.data;
  } catch (error) {
    console.error('Create alert error:', error);
    throw error;
  }
};

export const getAlerts = async () => {
  try {
    const response = await apiClient.get('/alerts');
    return response.data;
  } catch (error) {
    console.error('Fetch alerts error:', error);
    throw error;
  }
};
