import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ChatComponent } from './chat/chat.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, ChatComponent],
  template: `
    <div class="container mx-auto p-4">
      <h1 class="text-3xl font-bold mb-6 text-center">AI Chat App</h1>
      <app-chat></app-chat>
      <router-outlet></router-outlet>
    </div>
  `,
  styles: [`
    .container {
      max-width: 800px;
    }
  `]
})
export class App {}

