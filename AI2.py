from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "bert-base-cased-finetuned-mrpc"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


def check(sequence_0, sequence_1, verbose=False):
    tokens = tokenizer.encode_plus(sequence_0, sequence_1, return_tensors="pt")
    classification_logits = model(**tokens)[0]
    results = torch.softmax(classification_logits, dim=1).tolist()[0]

    if verbose:
        classes = ["not paraphrase", "is paraphrase"]
        for i in range(len(classes)):
            print(f"{classes[i]}: {round(results[i] * 100)}%")
    elif results[1] > 0.8:
        return True
    else:
        return False


if __name__ == '__main__':
    sequence_0 = "When two waves meet at a point, the resultant displacement at that point is equal to the sum of " \
                 "the displacements of the individual waves."
    sequence_1 = "when two waves meet the resultant displacement equalls the sum of the displacements of each wave"
    check(sequence_0, sequence_1, verbose=True)
