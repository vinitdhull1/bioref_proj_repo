
from simpletransformers.seq2seq import Seq2SeqModel, Seq2SeqArgs
from django.conf import settings




# Configure the model
model_args = Seq2SeqArgs()
model_args.num_train_epochs = 20
# model_args.no_save = True
model_args.max_length = 675
model_args.max_seq_length = 675
model_args.evaluate_generated_text = True
model_args.train_batch_size = 4
model_args.eval_batch_size = 4
model_args.evaluate_during_training = True
model_args.evaluate_during_training_verbose = True

    

# Loading a saved model
model = Seq2SeqModel(
    encoder_decoder_type="bart",
    #encoder_decoder_name="outputs/best_model/",
    encoder_decoder_name=r""+settings.MEDIA_ROOT+"best_model/",
    args=model_args,
    use_cuda=False,
)

def biorefOutput(text):
    return model.predict([text])[0]