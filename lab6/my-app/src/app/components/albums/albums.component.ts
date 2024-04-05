import { Component, OnInit } from '@angular/core';
import { CommonModule, NgForOf } from '@angular/common';
import { RouterModule } from '@angular/router';
import { AlbumService } from '../../services/album.service';
import { FormsModule } from '@angular/forms';
import { Album } from '../../models/album';

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './albums.component.html',
  styleUrl: './albums.component.css'
})
export class AlbumsComponent implements OnInit{
  albums!: Album[];
  newAlbum: Album;
  loaded: boolean = false;
  currentAlbum: Album | null = null;

  constructor(private AlbumService: AlbumService){
    this.newAlbum = {
      id: 1,
      title: "",
      body: ""
    }
  }

  ngOnInit(): void {
    this.getAlbums();
  }

  getAlbums() {
    this.loaded = false;
    this.AlbumService.getAlbums().subscribe((albums: Album[]) => {
      this.albums = albums;
      console.log(this.albums);
      this.loaded = true;
    });
  }

  deleteAlbum(id: number){
    this.albums = this.albums.filter((p) => p.id !== id);
  }

  addAlbum(){
      this.newAlbum.id = this.albums.length + 1;
      this.albums.push(this.newAlbum);
      alert('Album created succesfully!');
  }

}