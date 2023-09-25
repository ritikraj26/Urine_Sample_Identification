import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { ImageUploadService } from '../../services/image-upload/image-upload.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent {
  selectedFile: File | null = null;
  response: any;
  constructor(private imageUploadService: ImageUploadService) { }

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0] as File;
  }

  uploadImage() {
    if (this.selectedFile) {
      const formData = new FormData();
      formData.append('image', this.selectedFile);

      this.imageUploadService.uploadImage(formData).subscribe(
        (response) => {
          console.log('Image uploaded successfully', response);
          this.response = response;
        },
        (error) => {
          console.error('Error uploading image', error);
        }
      );
    }
  }
}