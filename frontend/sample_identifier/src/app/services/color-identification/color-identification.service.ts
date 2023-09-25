import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ColorIdentificationService {
  private baseUrl: string = 'http://localhost:8000/home/upload';

  constructor(private http: HttpClient) { }

  fetchColorResults(): Observable<any[]> {
    // const endpoint = `${this.baseUrl}api/color-identification`;
    return this.http.get<any[]>(this.baseUrl);
  }
}