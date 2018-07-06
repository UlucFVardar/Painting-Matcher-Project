# import the necessary packages
import numpy as np
import cv2
import argparse
import glob
import csv
import os
import argparse

# construct the argument parse and parse the arguments


class PaintingMatcher:
    def __init__(self, descriptor, paintingPaths, ratio = 0.7, minMatches = 40):
        self.descriptor = descriptor
        self.paintingPaths = paintingPaths   
        self.ratio = ratio
        self.minMatches = minMatches
        self.distanceMethod = "BruteForce"

    def search(self, queryKps, queryDescs):
        results = {}

        # loop over the painting images
        for paintingPath in self.paintingPaths:
            # load the query image, convert it to grayscale, and
            # extract keypoints and descriptors
            painting = cv2.imread(paintingPath)
            gray = cv2.cvtColor(painting, cv2.COLOR_BGR2GRAY)
            (kps, descs) = self.descriptor.describe(gray)

            # determine the number of matched, inlier keypoints,
            # then update the results
            score = self.match(queryKps, queryDescs, kps, descs)
            results[paintingPath] = score

        # if matches were found, sort them
        if len(results) > 0:
            results = sorted([(v, k) for (k, v) in results.items() if v > 0], reverse=True)

        return results

    def match(self, kpsA, featuresA, kpsB, featuresB):
        # compute the raw matches and initialize the list of actual
        # matches
        matcher = cv2.DescriptorMatcher_create(self.distanceMethod)
        rawMatches = matcher.knnMatch(featuresB, featuresA, 2)
        matches = []

        # loop over the raw matches
        for m in rawMatches:
            # ensure the distance is within a certain ratio of each
            # other
            if len(m) == 2 and m[0].distance < m[1].distance * self.ratio:
                matches.append((m[0].trainIdx, m[0].queryIdx))

        # check to see if there are enough matches to process
        if len(matches) > self.minMatches:
            # construct the two sets of points
            ptsA = np.float32([kpsA[i] for (i, _) in matches])
            ptsB = np.float32([kpsB[j] for (_, j) in matches])

            # compute the homography between the two sets of points
            # and compute the ratio of matched points
            (_, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, 4.0)

            # return the ratio of the number of matched keypoints
            # to the total number of keypoints
            return float(status.sum()) / status.size

        # no matches were found
        return -1.0

class PaintingDescriptor:

    def __init__(self):
        pass

    def describe(self, image):
        descriptor = cv2.xfeatures2d.SIFT_create()

        # detect keypoints in the image, describing the region
        # surrounding each keypoint, then convert the keypoints
        # to a NumPy array
        (kps, descs) = descriptor.detectAndCompute(image, None)
        kps = np.float32([kp.pt for kp in kps])

        return (kps, descs)


# MAIN PART---- NEED TO BE EDDITTED
# USAGE 
# python singlePage.py
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--PaintingPath", required=True,
    help="path to the image that you are looking for any information")
    args = vars(ap.parse_args())

    # initialize the database dictionary of paintings
    db = {}

    # loop over the database
    for l in csv.reader(open('database.csv')):
        # update the database using the image ID as the key
        db[l[0]] = l[1:]

    ratio = 0.7
    minMatches = 50

    #https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    # initialize the paintingDescriptor and paintingMatcher
    pd = PaintingDescriptor()
    pm = PaintingMatcher(pd, glob.glob(os.path.join('paintings', '*.png')) , ratio = ratio, minMatches = minMatches)


    # load the query image, convert it to grayscale, and extract
    # keypoints and descriptors
    queryImage = cv2.imread(args["PaintingPath"])  # the painting that user sent to server
    gray = cv2.cvtColor(queryImage, cv2.COLOR_BGR2GRAY)
    (queryKps, queryDescs) = pd.describe(gray)

    #prepareKpsDescriptor(queryKps, queryDescs) # print features of queryImage into a text file

    # try to match the book painting to a known database of images
    results = pm.search(queryKps, queryDescs)

    # show the query painting
    cv2.imshow("Query", queryImage)

    # check to see if no results were found
    if len(results) == 0:
        print("I could not find a match for that painting!")
        cv2.waitKey(0)

    # otherwise, matches were found
    else:
        # loop over the results
        for (i, (score, paintingPath)) in enumerate(results):
            # grab the book information
            (floor, paintingNo) = db[paintingPath[paintingPath.rfind("/") + 1:]]

            print("{}. {:.2f}% : {} - {}".format(i + 1, score * 100,
                floor, paintingNo))
            if i==0 :                 
                openFloorPlan(floor)

            # load the result image and show it
            #result = cv2.imread(paintingPath)
            ##cv2.imshow("Result", result)
            ##cv2.waitKey(0)
def openFloorPlan(name):
    f = open( name+'.txt', 'r')
    file_contents = f.read()
    print (file_contents)            
    f.close()



if __name__ == '__main__':
    main()