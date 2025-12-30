import * as dotenv from 'dotenv'; 

dotenv.config()

const getEnv = (key: string): string | undefined => {
    if (typeof process !== 'undefined' && process.env) {
        return process.env[key];
    }
    return undefined;
};

// env files
export const configuration = {
    API_KEY_FIREBASE: getEnv('apiKey'),
    AUTH_DOMAIN: getEnv('authDomain'), 
    PROJECT_ID: getEnv('projectId'),
    STORAGE_BUCKET: getEnv('storageBucket'),
    MESSAGING_SENDER_ID: getEnv('messagingSenderId'), 
    APP_ID: getEnv('appId')
}

export default configuration