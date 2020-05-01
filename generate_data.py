#!/usr/bin/env python

import argparse
import csv
import numpy as np
from numpy.random import shuffle

np.random.seed(123)  # for reproducibility


def load_templates(templates_file_path):
    templates = []
    with open(templates_file_path, "r") as file:
        for line in file:
            templates.append(line)
    return templates


def load_individuals(individuals_file_path):
    individuals_map = {}
    with open(individuals_file_path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        first_line = next(reader)
        for individuals_type in first_line:
            individuals_map["<"+individuals_type+">"] = []
    with open(individuals_file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            for type in first_line:
                if type in row:
                    if row[type] != "":
                        individuals_map["<"+type+">"].append(row[type])
    return individuals_map


def generate_data(templates, individuals, nb_examples_per_template=600):
    data = []
    already_generated = {}
    for temp in templates:
        for j in range(0, nb_examples_per_template):
            template_filled = fill_template(temp, individuals)
            if template_filled not in already_generated:
                data.append(template_filled)
            already_generated[template_filled] = True
    shuffle(data)
    return data


def fill_template(template, individuals):
    for key in individuals.keys():
        index = pick_index(individuals[key])
        individual = individuals[key][index]
        template = template.replace(key, individual)
        template = template.replace(" [none] ", " ")
        template = template.replace("[none] ", "")
        #template = template.lower()
    return template


def pick_index(sequence):
    return int((np.random.random_sample() * len(sequence)) % len(sequence))


def save(data, training_file_path, validation_file_path):
    nb_train = 0
    nb_val = 0
    with open(training_file_path, 'w') as train_file:
        with open(validation_file_path, 'w') as val_file:
            for line in data:
                if np.random.random_sample() > 0.333:
                    train_file.write(line)
                    nb_train += 1
                else:
                    val_file.write(line)
                    nb_val += 1
            print ("Saved "+str(nb_train)+" pairs in training dataset: "+training_file_path)
            print ("Saved "+str(nb_val)+" pairs in validation dataset: "+validation_file_path)


def main(templates_file_path="templates.csv", individuals_file_path="individuals.csv", max_examples_per_template=600, train_file="train.txt", val_file="val.txt"):
    templates = load_templates(templates_file_path)
    individuals = load_individuals(individuals_file_path)
    data = generate_data(templates, individuals, max_examples_per_template)
    save(data, train_file, val_file)
    print ("Bye bye !")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='The dataset generator.')
    parser.add_argument("--templates", type=str, default="templates.txt", help='The templates file to use')
    parser.add_argument("--individuals", type=str, default="individuals.csv", help='The individuals to randomly pick')
    parser.add_argument("--examples_per_template", type=int, default=1000, help="The max number of examples to generate per template")

    args = parser.parse_args()
    print ("Start generating dataset...")
    main(templates_file_path=args.templates, individuals_file_path=args.individuals, max_examples_per_template=args.examples_per_template)
