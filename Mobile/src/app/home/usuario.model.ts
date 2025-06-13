export class Usuario
{
  public id: number;
  public nome: string;
  public email: string;
  public token: string;

  constructor() { 
    this.id = 0;
    this.nome = '';
    this.email = '';
    this.token = '';
  }
}

// imports: [IonList, IonItem, IonInput, IonButton, IonContent, FormsModule],
// import { IonContent, LoadingController, NavController, AlertController, ToastController, IonList, IonItem, IonInput, IonButton } from '@ionic/angular/standalone';
//import { IonHeader, IonContent, IonButton, IonList, IonToolbar, IonTitle, IonItem, IonInput, NavController, AlertController, ToastController, LoadingController } 
//  imports: [IonList, IonHeader, IonItem, IonInput, IonContent, IonButton, FormsModule, IonToolbar, IonTitle],