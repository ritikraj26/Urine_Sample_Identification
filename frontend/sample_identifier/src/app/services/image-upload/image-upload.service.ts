import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ImageUploadService {
  private baseUrl: string = 'http://localhost:8000/home/upload/';

  constructor(private http: HttpClient) {}

  uploadImage(formData: FormData) {
    console.log(formData);
    return this.http.post(this.baseUrl, formData);
  }
}
