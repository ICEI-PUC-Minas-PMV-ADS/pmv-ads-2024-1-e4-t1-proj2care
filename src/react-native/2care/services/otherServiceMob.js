//import { sendAuthenticatedRequest } from "./authServiceMob.js";
import { API_URL } from './apiServiceMob.js';
import { sendAuthenticatedRequest } from './commonServiceMob'; // Importar apenas de commonServiceMob

const SERVICE_URL = "/core";

export const getGeolocationApi = async (post_code) => {
    try {
        const url = `${API_URL}${SERVICE_URL}/get/location/${post_code}`;
        const response = await sendAuthenticatedRequest(url);

        if (!response.ok) {
            const result = await response.json();
            throw new Error(JSON.stringify(result));
        }

        const result = await response.json();

        return {"latitude": Number(result["results"][0]["geometry"]["location"]["lat"].toFixed(6)), 
                "longitude": Number(result["results"][0]["geometry"]["location"]["lng"].toFixed(6))};
    } catch (error) {
        console.error("Erro ao buscar latitude e longitude:", error);
        throw new Error("CEP não pode ser validado, gentileza verificar o número.");
    }
};