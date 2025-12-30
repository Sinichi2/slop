import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  private apiUrl = 'http://localhost:3000/api';

  constructor(private http: HttpClient) {}

  sendMessage(message: string, image?: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/chat`, { message, image });
  }
}

