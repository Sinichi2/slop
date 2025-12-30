// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import configuration  from "../config";
import * as dotenv from 'dotenv';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: configuration.API_KEY_FIREBASE,
  authDomain: configuration.AUTH_DOMAIN,
  projectId: configuration.PROJECT_ID,
  storageBucket: configuration.STORAGE_BUCKET,
  messagingSenderId: configuration.MESSAGING_SENDER_ID,
  appId: configuration.APP_ID
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);