import { Component, ElementRef, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ChatService } from './chat.service';

interface Message {
  text: string;
  image?: string;
  isUser: boolean;
}

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <div class="chat-container border rounded-lg shadow-sm flex flex-col h-[600px] bg-white">
      <div class="chat-messages flex-1 overflow-y-auto p-4 space-y-4">
        <div *ngFor="let msg of messages" [ngClass]="{'text-right': msg.isUser, 'text-left': !msg.isUser}">
          <div [ngClass]="msg.isUser ? 'bg-blue-500 text-white' : 'bg-gray-200 text-black'" 
               class="inline-block p-3 rounded-lg max-w-[80%] break-words shadow-sm">
            <p *ngIf="msg.text">{{ msg.text }}</p>
            <img *ngIf="msg.image" [src]="msg.image" class="mt-2 max-w-full rounded-md shadow-sm border border-gray-300" />
          </div>
        </div>
      </div>
      
      <div class="p-4 border-t bg-gray-50 rounded-b-lg">
        <div *ngIf="pastedImage" class="relative inline-block mb-3 group">
          <img [src]="pastedImage" class="h-24 w-24 object-cover rounded-md border-2 border-blue-400 shadow-md" />
          <button (click)="clearImage()" 
                  class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center text-xs hover:bg-red-600 transition-colors shadow-sm">
            ✕
          </button>
        </div>
        
        <div class="flex gap-2">
          <input 
            #messageInput
            type="text" 
            [(ngModel)]="currentMessage" 
            (keydown.enter)="sendMessage()"
            (paste)="onPaste($event)"
            placeholder="Type a message or paste an image..."
            class="flex-1 border border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-shadow"
          />
          <button 
            (click)="sendMessage()" 
            [disabled]="!currentMessage && !pastedImage"
            class="bg-blue-500 text-white px-6 py-2 rounded-md hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed transition-colors font-medium"
          >
            Send
          </button>
        </div>
        <p class="text-xs text-gray-400 mt-2 italic">Tip: You can paste images directly into the input field.</p>
      </div>
    </div>
  `,
  styles: [`
    :host {
      display: block;
    }
    .chat-messages {
      scrollbar-width: thin;
      scrollbar-color: #cbd5e0 #f7fafc;
    }
    .chat-messages::-webkit-scrollbar {
      width: 6px;
    }
    .chat-messages::-webkit-scrollbar-track {
      background: #f7fafc;
    }
    .chat-messages::-webkit-scrollbar-thumb {
      background-color: #cbd5e0;
      border-radius: 20px;
    }
  `]
})
export class ChatComponent {
  messages: Message[] = [];
  currentMessage = '';
  pastedImage: string | null = null;

  @ViewChild('messageInput') messageInput!: ElementRef;

  constructor(private chatService: ChatService) {}

  onPaste(event: ClipboardEvent) {
    const items = event.clipboardData?.items;
    if (!items) return;

    for (let i = 0; i < items.length; i++) {
      if (items[i].type.indexOf('image') !== -1) {
        const blob = items[i].getAsFile();
        if (blob) {
          const reader = new FileReader();
          reader.onload = (e: any) => {
            this.pastedImage = e.target.result;
          };
          reader.readAsDataURL(blob);
          event.preventDefault(); // Prevent text paste if it was an image
        }
      }
    }
  }

  clearImage() {
    this.pastedImage = null;
  }

  sendMessage() {
    if (!this.currentMessage && !this.pastedImage) return;

    const userMsg: Message = {
      text: this.currentMessage,
      image: this.pastedImage || undefined,
      isUser: true
    };

    this.messages.push(userMsg);

    const msgToSend = this.currentMessage;
    const imgToSend = this.pastedImage || undefined;

    this.currentMessage = '';
    this.pastedImage = null;

    this.chatService.sendMessage(msgToSend, imgToSend).subscribe({
      next: (response) => {
        this.messages.push({
          text: response.reply,
          isUser: false
        });
      },
      error: (err) => {
        console.error('Error sending message:', err);
        this.messages.push({
          text: 'Error: Could not reach the backend. Make sure the Node.js server is running.',
          isUser: false
        });
      }
    });
  }
}

