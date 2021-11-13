import os
import cv2
import numpy as np

def get_homography(from_points, to_points):
    H, _ = cv2.findHomography(from_points, to_points)
    return H

def project_points(points, H, I, J):
    """
    @param I: original image
    @param J: top view image
    @param H: homography
    """
    for point in points:
        W = H[2,0]*point[0] + H[2,1]*point[1] + H[2,2]
        top_point = [(H[0,0]*point[0] + H[0,1]*point[1] + H[0,2])/W,
                    (H[1,0]*point[0] + H[1,1]*point[1] + H[1,2])/W]
        # print(top_point)

        if top_point[0] <= 0: top_point[0] = 100
        if top_point[1] <= 0: top_point[1] = 100

        cv2.circle(I, (int(top_point[0]), int(top_point[1])), 2, (0,0,255), 2)
        cv2.circle(J, (int(point[0]), int(point[1])), 2, (0,0,255), 2)


def create_homography(pitch_cord,view):
    top_points={}
    full_points={}
    #bottom_down and Top_down { anti clock from bottom_left}
    top_points["1"]= np.asarray([
        [1355, 1542],
        [1424, 1542],
        [1424, 1108],
        [1355, 1108],
        ], dtype=np.float32)

    #bottom_down and Top_up { anti clock from bottom_left}
    top_points["2"]= np.asarray([
        [1355, 1542],
        [1424, 1542],
        [1424, 1080],
        [1355, 1080],
        ], dtype=np.float32)

    #bottom_up and Top_down { anti clock from bottom_left}
    top_points["3"]= np.asarray([
        [1355, 1514],
        [1424, 1514],
        [1424, 1108],
        [1355, 1108],
        ], dtype=np.float32)

    #bottom_up and Top_up { anti clock from bottom_left}
    top_points["4"]= np.asarray([
        [1355, 1514],
        [1424, 1514],
        [1424, 1080],
        [1355, 1080],
        ], dtype=np.float32)


    #right being (  right from where we entered ground)
#left being ( left from where we entered ground)
    # full_points["left"] = np.asarray([
        # [2989, 1113],  
        # [2907, 1101],  
        # [2154, 1141],  
        # [2220, 1156]   
    #     ], dtype=np.float32)

    # #center being (  nearly center from where we entered ground)
    # full_points["center"] = np.asarray([
    #     [2030, 1030],
    #     [2189, 1033],
    #     [2111, 937],
    #     [1981, 935]
    #     ], dtype=np.float32)

    # #right being (  right from where we entered ground)
    # full_points["right"] = np.asarray([
    #     [1875, 1014],
    #     [1827, 1022],
    #     [2368, 1061],
    #     [2409, 1051]
    #     ], dtype=np.float32)

    full_points[view] = np.asarray( pitch_cord, dtype=np.float32)
    

    I = cv2.imread("static/images/cricket_elong.png")

    views = ["left" , "center" , "right"]

    for num in range(1,5):

        J = cv2.imread("static/images/" + view + ".jpg")
        # print(J)
        # print("static/images/sample_"+view+".jpg")
        top_points_local = top_points[str(num)]
        top_points_local = 500+top_points_local*(1700/2700) #added 400 because we padded pitch

        H1 = get_homography(full_points[view], top_points_local)
        try: 
            os.system("mkdir static/images/projections")
            os.system("mkdir static/images/projections/"+view)
        except Exception as e:
            print(e)

        project_points(full_points[view], H1, I, J)
        cv2.imwrite("static/images/projections/"+view+"/I.jpg", J)
        cv2.imwrite("static/images/projections/"+view+"/HI.jpg", H1)

        K1 = cv2.warpPerspective(J, H1, (I.shape[1], I.shape[0])) 
        cv2.imwrite("static/images/projections/"+view+"/full_warped"+str(num)+".jpg", K1+I)


# create_homography([[2989, 1113],  
#         [2907, 1101],  
#         [2154, 1141],  
#         [2220, 1156]] , 'left')