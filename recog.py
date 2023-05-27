import face_recognition as fr



def recognize(face,known_faces):
    min_match=0
    matched_name=None
    for person in known_faces.keys():
        matches=0
        for kface_embed in (known_faces[person]):
            result=fr.compare_faces(kface_embed,face,0.4)
            if result[0]==True:
                matches+=1
        if min_match < matches:
            min_match=matches
            matched_name=person

    return matched_name

def detect_face(img):
     return fr.face_locations(img=img,model="hog")

def recognize_face(img,known_faces):
    match=None
    unknown_face=fr.face_encodings(img)
    if unknown_face:
        match=recognize(unknown_face[0],known_faces)

    return match