import { Album } from "../models/album";

export const Albums: Album[] =[];

for(let i = 0; i < 10; i++){
    Albums.push(
        {
            id: i+1,
            title: `title ${i+1}`,
            body: 'Body'

        }
    )
}