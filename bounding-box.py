#!/usr/bin/env python

"""Calculate a bounding box for the whole GPX file."""

import sys
import gpxpy


def main():
    input = sys.argv[1:]
    if not input:
        sys.exit(f"usage: {__file__} INPUT_FILE")

    gpx_files = []
    for fn in input:
        with open(fn) as fin:
            gpx_files.append(gpxpy.parse(fin))

    bbox = None

    for gpx in gpx_files:
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
