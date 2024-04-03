import { Component, OnInit } from '@angular/core';
import { CommonModule, NgForOf } from '@angular/common';
import { RouterModule } from '@angular/router';
import { AlbumService } from '../services/album.service';
import { FormsModule } from '@angular/forms';
import { Album } from '../models/album';

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './albums.component.html',
  styleUrl: './albums.component.css'
})
export class AlbumsComponent implements OnInit{
  albums!: Album[];
  newAlbum?: Album;
  loaded: boolean = false;
  currentAlbum: Album | null = null;

  constructor(private AlbumService: AlbumService){}

  ngOnInit(): void {
    this.getAlbums();
  }

  getAlbums(){
    this.loaded = false;
    this.AlbumService.getAlbums().subscribe((albums: Album[]) => {
      this.albums = albums;
      this.loaded = true;
    });

  }

  deleteAlbum(id: number){
    this.albums = this.albums.filter((p) => p.id !== id);
    this.AlbumService.deleteAlbum(id).subscribe(() => {
      console.log('deleted');
    });
}

  addAlbum(){
    this.AlbumService.createAlbum(
        this.newAlbum ?? {}
    ).subscribe((album : Album)=>{
            console.log(album);
            this.albums.push(album);
            alert('Album created succesfully!');
            this.newAlbum = {};
        }
    );
  }

  updateAlbum(): void {
    if (!this.currentAlbum) return;
  
    this.AlbumService.updateAlbum(
        this.currentAlbum.id!, 
        this.currentAlbum
    ).subscribe((updatedAlbum: Album) => {
            const index = this.albums.findIndex(a => a.id === updatedAlbum.id);
            if (index !== -1) {
              this.albums[index] = updatedAlbum; 
            }
            this.currentAlbum = null; 
            alert('Album updated successfully!');
        }
    );
}
}