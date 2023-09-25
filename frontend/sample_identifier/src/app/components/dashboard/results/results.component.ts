import { Component, OnInit } from '@angular/core';
import { ColorIdentificationService } from 'src/app/services/color-identification/color-identification.service';


@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent {
  // colorResults: any[] = [];

  // constructor(private colorIdentificationService: ColorIdentificationService) { }

  // ngOnInit(): void {
  //   this.fetchColorResults();
  // }
  // fetchColorResults() {
  //   this.colorIdentificationService.fetchColorResults().subscribe(
  //     (results) => {
  //       this.colorResults = results;
  //     },
  //     (error) => {
  //       console.error('Error fetching color results:', error);
  //     }
  //   );
  // }
}
