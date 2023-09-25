import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UploadComponent } from './components/dashboard/upload/upload.component';
import { ResultsComponent } from './components/dashboard/results/results.component';
// import { Routes } from '@angular/router';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { HttpClientModule } from '@angular/common/http';

// const routes: Routes = [
//   { path: '', component: UploadComponent },
//   { path: '', component: ResultsComponent },
// ]

@NgModule({
  declarations: [
    AppComponent,
    UploadComponent,
    ResultsComponent,
    DashboardComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
