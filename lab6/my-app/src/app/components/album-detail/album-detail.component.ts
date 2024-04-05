import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { Album } from '../../models/album';
import { AlbumService } from '../../services/album.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [RouterModule, CommonModule, FormsModule],
  templateUrl: './album-detail.component.html',
  styleUrl: './album-detail.component.css'
})
export class AlbumDetailComponent implements OnInit{
  newAlbum: Album;
  album!: Album;
  loaded: boolean = false;
  constructor(private route: ActivatedRoute, private albumService: AlbumService){
    this.newAlbum = {
      id: 1,
      title: "",
      body: ""
    }
  }
  ngOnInit(): void {
    this.getAlbum();
  }

  getAlbum(){
    this.route.paramMap.subscribe((params) => {
      const albumId = Number(params.get('albumId'));
      this.loaded = false;
      this.albumService.getAlbum(albumId).subscribe((album) => {
        this.album = album;
        this.newAlbum = {
          id: album.id,
          title: album.title,
          body: album.body,
        };
        this.loaded = true;
      })      
    })

  }

  updateAlbum() {
      this.album = this.newAlbum;
  }

}