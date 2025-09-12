Typescript
import { browser, $ } from '@wdio/globals';
import { expect } from 'chai';
describe('FR-04: Custom Landing Pages Creation', () => {
    before(async () => { await browser.url('http://www.ipsy.com/admin/landing-create'); });
    it('Positive - Verify that custom landing pages can be successfully created', async () => {
        const createForm = await $('.create-form');
        await expect(createForm).toBeDisplayed();
        const detailsInput = await $('.campaign-details');
        await detailsInput.setValue('Campaign1');
        const saveButton = await $('.save-landing');
        await saveButton.click();
        const uniqueUrl = await $('.unique-url');
        await expect(uniqueUrl).toBeDisplayed();
    });
    it('Negative - Verify creation fails with duplicate campaign details', async () => {
        const detailsInput = await $('.campaign-details');
        await detailsInput.setValue('ExistingCampaign');
        const saveButton = await $('.save-landing');
        await saveButton.click();
        const errorMessage = await $('.error-message');
        await expect(errorMessage).toBeDisplayed();
    });
    it('Edge - Verify creation with minimal details', async () => {
        const detailsInput = await $('.campaign-details');
        await detailsInput.setValue('A');
        const saveButton = await $('.save-landing');
        await saveButton.click();
        const uniqueUrl = await $('.unique-url');
        await expect(uniqueUrl).toBeDisplayed();
    });
});
