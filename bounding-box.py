#!/usr/bin/env python

"""Calculate a bounding box for the whole GPX file."""

import sys
import gpxpy


def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        sys.exit(f"usage: {__file__} INPUT_FILE")

    with open(filename) as fin:
        gpx = gpxpy.parse(fin)

    bbox = None

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if bbox is None:
                    bbox = (point.longitude, point.latitude,
                            point.longitude, point.latitude)
                else:
                    left, top, right, bottom = bbox
                    left = min(left, point.longitude)
                    right = max(right, point.longitude)
                    top = max(top, point.latitude)
                    bottom = min(bottom, point.latitude)
                    bbox = left, top, right, bottom
    print(",".join(str(n) for n in bbox))


if __name__ == '__main__':
    main()
