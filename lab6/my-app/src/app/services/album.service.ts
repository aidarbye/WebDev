import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Album } from '../models/album';
import { Photo } from '../models/photo';

@Injectable({
  providedIn: 'root'
})
export class AlbumService {
  
    constructor(private client: HttpClient) { }

    getAlbums(): Observable<Album[]>{
        return this.client.get<Album[]>('https://jsonplaceholder.typicode.com/albums');
    }

    getAlbum(id: number): Observable <Album>{
        return this.client.get<Album>(`https://jsonplaceholder.typicode.com/albums/${id}`);
    }

    getPhoto(id: number) {
        return this.client.get<Photo[]>(`https://jsonplaceholder.typicode.com/albums/${id}/photos`);
    }
}