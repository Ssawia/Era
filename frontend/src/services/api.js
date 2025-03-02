import axios from 'axios';

// Create an instance of axios with the base URL
const api = axios.create({
  baseURL: "http://localhost:8000"
});


export const getCharacters = async () => {
  try {
    const response = await api.get('/characters');
    return response
  
  } catch (error) {
    console.error("Error fetching characters", error);
  }
};

export const addCharacters = async (fruitName) => {
  try {
    await api.post('/fruits', { name: fruitName });
    getCharacters();  // Refresh the list after adding a fruit
  } catch (error) {
    console.error("Error adding fruit", error);
  }
};


// Export the Axios instance
export default api;